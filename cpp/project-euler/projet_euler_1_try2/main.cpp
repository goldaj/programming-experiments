#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define N3 ((input[i] - 1) / 3)
#define N5 ((input[i] - 1) / 5)
#define N15 ((input[i] - 1) / 15)

#define C3 (N3 * (N3 + 1) / 2) * 3
#define C5 (N5 * (N5 + 1) / 2) * 5
#define C15 (N15 * (N15 + 1) / 2) * 15

int main() {
	long long i, t;
	cin >> t;
	vector<long long> input(t);
	for(i = 0; i < t; i += 1) {
		cin >> input[i];
	}
	for(i = 0; i < t; i += 1) {
		cout << C3 + C5 - C15 << endl;
	}
    return 0;
}
