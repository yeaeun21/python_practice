#include <stdio.h>
#include <stdlib.h>
#include<time.h>
#define SWAP(a,b)  {int t; t = a; a=b; b=t;}//a�� b�� ��ȯ

void SelectionSort(int *base, int n);
int theLargest(int *arr, int last);
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

	SelectionSort(arr, 10);
	theLargest(arr, 10);
	return 0;
}
void Array(int *arr, int n);
void SelectionSort(int *base, int n) //�迭 �� �� ���� ū���� ������ �� ��ȯ
{
	int last, j;
	int k;
	Array(base, n);//���� ���� ���

	for (last = n; last > 1; last--)//������ ������ ������ �ϳ��� ���
	{
		k = 0;
		for (j = 0; j < last; j++)
		{
			k = theLargest(base, last);
			SWAP(base[k], base[last - 1]);//��ȯ
		}

		Array(base, n);//���� ���
	}
}
int theLargest(int *arr, int last) { //�迭 �� ����ū ���� �ε����� ����
	int largest = 1;
	int i;
	for (i = 0; i < last; i++) {
		if (arr[i] > arr[largest]) {
			largest = i;
		}
	}
	return largest;
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