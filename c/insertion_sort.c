#include <stdio.h>
#define SWAP(a,b)  {int t; t = a; a=b; b=t;}//a와 b를 교환

void InsertionSort(int *base, int n);

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


	InsertionSort(arr, 10);

	return 0;
}

void Array(int *arr, int n);

void InsertionSort(int *base, int n)
{
	int i, loc;

	Array(base, n);//현재 상태 출력
	for (i = 1; i < n; i++)//정렬할 범위를 확대해 나갑니다.
	{
		for (loc = i; loc > 0; loc--)
		{
			if (base[loc - 1] > base[loc])//앞쪽 원소가 더 크면
			{
				SWAP(base[loc - 1], base[loc]);//교환
				Array(base, n);//상태 출력
			}
			else
			{
				break;
			}
		}
	}
}



void Array(int *arr, int n)//정렬되는 배열을 출력
{
	int i = 0;
	for (i = 0; i < n; i++)
	{
		printf("%2d ", arr[i]);
	}
	printf("\n");
}
