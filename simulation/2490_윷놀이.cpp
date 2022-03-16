#include <iostream>
#include <vector>

using namespace std;

int main() {
	int list[3][4] = {};

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 4; j++) {
			cin >> list[i][j];
		}
	}
	
	for (int i = 0; i < 3; i++) {
		int sum = 0;
		for (int j = 0; j < 4; j++) {
			sum += list[i][j];
		}
		switch (sum) {
		case 0: 
			cout << "D" << endl;
			break;
		case 1:
			cout << "C" << endl;
			break;
		case 2:
			cout << "B" << endl;
			break;
		case 3:
			cout << "A" << endl;
			break;
		case 4:
			cout << "E" << endl;
			break;

		}
	}

	return 0;
}
