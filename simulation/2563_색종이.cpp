#include <iostream>

using namespace std;

int main() {

	int map[100][100] = { 0 };
	int row, col, n;
	int ans = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> row >> col;
		for (int c = col; c < col + 10; c++) {
			for (int r = row; r < row + 10; r++) {
				if (map[c][r] == 1) continue;
				else {
					map[c][r] = 1;
					ans++;
				}
			}
		}
	}
	cout << ans;
	return 0;
}
