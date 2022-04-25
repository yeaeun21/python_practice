#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#define SWAP(a,b)  {int t; t = a; a=b; b=t;}//a�� b�� ��ȯ

int *A;
int on;

void MergeSort(int *base, int n);
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

	A = arr;
	on = 10;
	Array(A, on);
	MergeSort(arr, 10);
	Array(A, on);
	return 0;
}



void PrintSpace(int n);
void MergeSort(int *base, int n)
{
	int half_a = n / 2; //�迭�� �߰����� ���� ���� 
	int half_b = n - half_a; //�迭�� �߰����� ���� ����
	int ai = 0, bi = half_a;
	int i = 0;
	int *m = 0;

	if (n <= 1)//�迭�� ũ�Ⱑ 1���� �۰ų� ���� ��
	{
		return;
	}

	MergeSort(base, half_a);//���� �迭 ����
	PrintSpace(base - A);
	Array(base, half_a);
	MergeSort(base + half_a, half_b);//���� �迭 ����
	PrintSpace(base + half_a - A);
	Array(base + half_a, half_b);

	m = (int *)malloc(sizeof(int)*n);//�迭 ũ���� �ӽ� ������ �Ҵ�
	memcpy(m, base, sizeof(int)*n);//�ӽ� ������ �迭 �޸� ����

	while ((ai < half_a) && (bi < n))
	{
		if (m[ai] <= m[bi])//������ ũ�ų� ���� ��
		{
			base[i] = m[ai];//���� �迭�� ���Ҹ� ����
			ai++;
		}
		else
		{
			base[i] = m[bi];//���� �迭�� ���Ҹ� ����
			bi++;
		}
		i++;
	}

	while (ai < half_a)//���� �迭�� ���� �͵��� ����
	{
		base[i] = m[ai];
		i++;
		ai++;
	}

	while (bi < n)//���� �迭�� ���� �͵��� ����
	{
		base[i] = m[bi];
		i++;
		bi++;
	}
	free(m);// �޸� ����       
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
