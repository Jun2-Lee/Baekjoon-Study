#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct nation {
	int name;
	int gold;
	int silver;
	int bronze;
};
int main() {
	int n, ans, idx, rank;
	vector<nation> n_list;
	cin >> n >> ans;
	for (int i = 0; i < n; i++) {
		nation temp;
		cin >> temp.name >> temp.gold >> temp.silver >> temp.bronze;
		n_list.push_back(temp);
	}
	
	for (int i = 0; i < n; i++) {
		if (n_list[i].name == ans) {
			idx = i;
			break;
		}
	}

	for (int i = 0; i < n; i++) {
		if (n_list[i].gold > n_list[idx].gold)
			rank++;
		else if (n_list[i].gold == n_list[idx].gold) {
			if (n_list[i].silver > n_list[idx].silver)
				rank++;
			else if (n_list[i].silver == n_list[idx].silver) {
				if (n_list[i].bronze > n_list[idx].bronze)
					rank++;
			}
		}
	}
	cout << rank + 1;
	return 0;
}
