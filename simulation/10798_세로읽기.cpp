#include <iostream>
#include <vector>

using namespace std;

int main() {
	vector <vector<char>> list;
	int max_count = 0;
	for (int i = 0; i < 5; i++) {
		string temp;
		vector <char> temp_list;
		cin >> temp;
		for (int j = 0; j < temp.size(); j++) {
			temp_list.push_back(temp[j]);
			if(temp.size() > max_count) max_count = temp.size();
		}
		list.push_back(temp_list);
	}
	for (int i = 0; i < max_count; i++) {
		for (int j = 0; j < 5; j++) {
			if (list[j].size() > i ) {
				cout << list[j][i];
			}
		}
	}

	return 0;
}
