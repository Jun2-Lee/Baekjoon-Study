#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

	int n1, n2, t;
	cin >> n1 >> n2;
	vector <pair<char, bool>> ant;

	string ant1, ant2;
	cin >> ant1;
	reverse(ant1.begin(), ant1.end());
	for (int i = 0; i < n1; i++) {
		pair<char, bool> temp;
		temp.second = true;
		temp.first = ant1[i];
		ant.push_back(temp);
	}

	cin >> ant2;
	for (int i = 0; i < n2; i++) {
		pair<char, bool> temp;
		temp.second = false;
		temp.first = ant2[i];
		ant.push_back(temp);
	}

	cin >> t;
	for (int i = 0; i < t; i++) {
		for (int j = 0; j < ant.size()-1; j++) {
			if (ant[j].second == true && ant[j + 1].second == false) {
				swap(ant[j], ant[j + 1]);
				j++;
			}
		}
	}

	for (int i = 0; i < ant.size(); i++) {
		cout << ant[i].first;
	}

	return 0;
}
