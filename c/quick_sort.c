#include <stdio.h>
#define SWAP(a,b)  {int t; t = a; a=b; b=t;}//a�� b�� ��ȯ

int *origin;
int on;

void QuickSort(int *base, int n);
void Array(int *arr, int n);

int main(void)
{
	int i;
	int arr[10];
	//srand(time(NULL)); //�������� ���ڸ� �� 10�� ����
	//for (k = 0; k < 10; k++) {
	//	arr[k] = rand() % 89 + 10;
	//}
	printf("���ڸ� �� 10���� �Է��ϼ���:\n"); //���ڸ� �� 10�� ����ڿ��� �Է¹ޱ�
	for (i = 0; i < 10; i++) {
		scanf_s("%d", &arr[i]);
	};

	origin = arr;
	on = 10;
	Array(arr, 10);
	QuickSort(arr, 10);
	Array(arr, 10);

	return 0;
}

void PrintSpace(int n);
void QuickSort(int *base, int n)
{
	int p = 0; // ���� ���Ҹ� ����ϱ� ���� ����
	int left = 0, right = 0; // ���ؿ��Һ��� ū ���� ���� ���� ��ġ�� ã������ ����

	if (n <= 1)
	{
		return;
	}

	left = 0;
	right = n;

	while (1) //�ݺ�
	{
		for (left++; (left < n) && (base[0] >= base[left]); left++); //���� ���� �������� �����ϱ� ���ؼ� left����, ���� ���ؿ��Һ��� ū ���� ���� ������ left�̵�

		for (right--; (right > 0) && (base[0] < base[right]); right--); //���ʿ� ���ؿ��Һ��� ���� ���� ���� ������ right�� �̵�

		if (left < right) //left�� right���� �۴ٸ� ���ؿ��Һ���  ���� ���� ū ������ �ڿ� �����ϱ� ��ȯ
		{
			SWAP(base[left], base[right]);
			PrintSpace(base - origin);
			Array(base, n);
		}
		else //���ؿ��Ҹ� �߽����� ū ���� ���� �� �и� �Ϸ�
		{
			break;
		}
	}

	SWAP(base[0], base[right]); //���ؿ��Ҹ� �и��� ���� ���� ū �� ���̷� ����
	PrintSpace(base - origin);
	Array(base, n);

	QuickSort(base, right); //���ؿ��Һ��� ���� ���� �ִ� ���� ����
	QuickSort(base + left, n - left); //���ؿ��Һ��� ū ���� �ִ� ���� ����

}

void PrintSpace(int n)
{
	int i = 0;

	for (i = 0; i < n; i++)
	{
		printf("   ");
	}
}

void Array(int *arr, int n) //���ĵǴ� �迭�� ���
{
	int i = 0;
	for (i = 0; i < n; i++)
	{
		printf("%2d ", arr[i]);
	}
	printf("\n");
}

