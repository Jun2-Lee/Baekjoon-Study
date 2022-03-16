#include <iostream>

using namespace std;

int main() {

	int hour, minute;
	bool flag = false;
	cin >> hour >> minute;
	
	if (minute < 45) {
		minute += 15;
		flag = true;
	}
	else minute -= 45;

	if (flag) {
		if (hour == 0) hour = 23;
		else hour -= 1;
	}
	cout << hour << " " << minute;

	return 0;
}
