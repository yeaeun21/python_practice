#include <stdio.h>
#define SWAP(a,b)  {int t; t = a; a=b; b=t;}//a�� b�� ��ȯ

void bubbleSort(int *base, int n);

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

	bubbleSort(arr, 10);
	return 0;
}

void Array(int *arr, int n);
void bubbleSort(int *base, int n)
{
	int last, j;
	Array(base, n);//���� ���� ���

	for (last = n; last > 1; last--)//������ ������ ���
	{	
		for (j = 1; j < last - 1; j++)//�ݺ�
		{
			if (base[j] > base[j + 1])//���� ���Ұ� �� ũ��
			{
				SWAP(base[j], base[j + 1]);//��ȯ
				Array(base, n);//���� ���
			}
		}
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