#include<iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int a;
	cin >> a;
	int num1,num2,temp;
	int cycle = 0;
	temp = a;
	while (1) {
		num2 = (temp % 10 + temp/10)%10;
		num1 = temp % 10;
		temp = 10 * num1 + num2;
		cycle++;
		if (temp== a)
			break;
	}
	cout << cycle;

	return 0;
}
