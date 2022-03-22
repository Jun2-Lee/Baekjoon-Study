#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int choice(string s) {
	string list[8] = { "R", "L","B","T","RT","LT","RB", "LB" };
	for (int i = 0; i < 8; i++) {
		if (s == list[i]) return i;
	}
	return 0;
}
int main() {
	int map[8][8] = { 0 };
	string king, stone;
	int n;
	cin >> king >> stone >> n;
	int king_col = int(king[0]) - 65;
	int king_row = int(king[1]) - 49;
	int stone_col = int(stone[0]) - 65;
	int stone_row = int(stone[1]) - 49;
	for (int i = 0; i < n; i++) {
		int temp_col, temp_row;
		string s;
		cin >> s;
		int num = choice(s);
		switch (num) {
		case 0:
			temp_col = king_col + 1; temp_row = king_row;
			if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
			if (temp_col == stone_col && temp_row == stone_row) {
				temp_col = stone_col + 1; temp_row = stone_row;
				if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
				stone_col++;
			}
			king_col++;
			break;
		case 1:
			temp_col = king_col - 1; temp_row = king_row;
			if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
			if (temp_col == stone_col && temp_row == stone_row) {
				temp_col = stone_col - 1; temp_row = stone_row;
				if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
				stone_col--;
			}
			king_col--;
			break;
		case 2:
			temp_col = king_col; temp_row = king_row - 1;
			if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
			if (temp_col == stone_col && temp_row == stone_row) {
				temp_col = stone_col; temp_row = stone_row - 1;
				if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
				stone_row--;
			}
			king_row--;
			break;
		case 3:
			temp_col = king_col; temp_row = king_row + 1;
			if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
			if (temp_col == stone_col && temp_row == stone_row) {
				temp_col = stone_col; temp_row = stone_row + 1;
				if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
				stone_row++;
			}
			king_row++;
			break;
		case 4:
			temp_col = king_col + 1; temp_row = king_row + 1;
			if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
			if (temp_col == stone_col && temp_row == stone_row) {
				temp_col = stone_col + 1; temp_row = stone_row + 1;
				if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
				stone_col++; stone_row++;
			}
			king_col++; king_row++;
			break;
		case 5:
			temp_col = king_col - 1; temp_row = king_row + 1;
			if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
			if (temp_col == stone_col && temp_row == stone_row) {
				temp_col = stone_col - 1; temp_row = stone_row + 1;
				if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
				stone_col--; stone_row++;
			}
			king_col--; king_row++;
			break;
		case 6:
			temp_col = king_col + 1; temp_row = king_row - 1;
			if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
			if (temp_col == stone_col && temp_row == stone_row) {
				temp_col = stone_col + 1; temp_row = stone_row - 1;
				if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
				stone_col++; stone_row--;
			}
			king_col++; king_row--;
			break;
		case 7:
			temp_col = king_col - 1; temp_row = king_row - 1;
			if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
			if (temp_col == stone_col && temp_row == stone_row) {
				temp_col = stone_col - 1; temp_row = stone_row - 1;
				if (temp_col < 0 || temp_col >= 8 || temp_row < 0 || temp_row >= 8) break;
				stone_col--; stone_row--;
			}
			king_col--; king_row--;
		}
	}
	king[0] = king_col + 65;
	king[1] = king_row + 49;
	stone[0] = stone_col + 65;
	stone[1] = stone_row + 49;
	cout << king << endl << stone;
	return 0;
}
