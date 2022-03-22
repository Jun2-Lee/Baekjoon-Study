#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N, L, ans = 0, pos = 0;
	cin >> N >> L;
	int d, r, g;
	for (int i = 0; i < N; i++) {
		cin >> d >> r >> g;
		ans += (d - pos);
		pos = d;
		if (ans % (r + g) < r) ans += r - ans % (r + g);
	}
	ans += L - pos;
	cout << ans;
	return 0;
}
