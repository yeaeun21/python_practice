#include <stdio.h>
#define SWAP(a,b)  {int t; t = a; a=b; b=t;}//a�� b�� ��ȯ

void InsertionSort(int *base, int n);

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


	InsertionSort(arr, 10);

	return 0;
}

void Array(int *arr, int n);

void InsertionSort(int *base, int n)
{
	int i, loc;

	Array(base, n);//���� ���� ���
	for (i = 1; i < n; i++)//������ ������ Ȯ���� �����ϴ�.
	{
		for (loc = i; loc > 0; loc--)
		{
			if (base[loc - 1] > base[loc])//���� ���Ұ� �� ũ��
			{
				SWAP(base[loc - 1], base[loc]);//��ȯ
				Array(base, n);//���� ���
			}
			else
			{
				break;
			}
		}
	}
}



void Array(int *arr, int n)//���ĵǴ� �迭�� ���
{
	int i = 0;
	for (i = 0; i < n; i++)
	{
		printf("%2d ", arr[i]);
	}
	printf("\n");
}
