#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#define SWAP(a,b)  {int t; t = a; a=b; b=t;}//a와 b를 교환

int *A;
int on;

void MergeSort(int *base, int n);
void Array(int *arr, int n);

int main(void)
{
	int i;
	int arr[10];
	//srand(time(NULL)); //랜덤으로 두자릿 수 10개 생성
	//for (k = 0; k < 10; k++) {
	//	arr[k] = rand() % 89 + 10;
	//}
	printf("두자릿 수 10개를 입력하세요:\n"); //두자릿 수 10개 사용자에게 입력받기
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
	int half_a = n / 2; //배열의 중간지점 앞쪽 개수 
	int half_b = n - half_a; //배열의 중간지점 뒤쪽 개수
	int ai = 0, bi = half_a;
	int i = 0;
	int *m = 0;

	if (n <= 1)//배열의 크기가 1보다 작거나 같을 때
	{
		return;
	}

	MergeSort(base, half_a);//앞쪽 배열 정렬
	PrintSpace(base - A);
	Array(base, half_a);
	MergeSort(base + half_a, half_b);//뒤쪽 배열 정렬
	PrintSpace(base + half_a - A);
	Array(base + half_a, half_b);

	m = (int *)malloc(sizeof(int)*n);//배열 크기의 임시 공간을 할당
	memcpy(m, base, sizeof(int)*n);//임시 공간에 배열 메모리 복사

	while ((ai < half_a) && (bi < n))
	{
		if (m[ai] <= m[bi])//뒤쪽이 크거나 같을 때
		{
			base[i] = m[ai];//앞쪽 배열의 원소를 대입
			ai++;
		}
		else
		{
			base[i] = m[bi];//뒤쪽 배열의 원소를 대입
			bi++;
		}
		i++;
	}

	while (ai < half_a)//앞쪽 배열의 남은 것들을 대입
	{
		base[i] = m[ai];
		i++;
		ai++;
	}

	while (bi < n)//뒤쪽 배열의 남은 것들을 대입
	{
		base[i] = m[bi];
		i++;
		bi++;
	}
	free(m);// 메모리 해제       
}

void PrintSpace(int n)
{
	int i = 0;
	for (i = 0; i < n; i++)
	{
		printf("   ");
	}
}

void Array(int *arr, int n) //정렬되는 배열을 출력
{
	int i = 0;
	for (i = 0; i < n; i++)
	{
		printf("%2d ", arr[i]);
	}
	printf("\n");
}
