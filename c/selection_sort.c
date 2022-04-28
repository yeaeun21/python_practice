#include <stdio.h>
#include <stdlib.h>
#include<time.h>
#define SWAP(a,b)  {int t; t = a; a=b; b=t;}//a와 b를 교환

void SelectionSort(int *base, int n);
int theLargest(int *arr, int last);
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

	SelectionSort(arr, 10);
	theLargest(arr, 10);
	return 0;
}
void Array(int *arr, int n);
void SelectionSort(int *base, int n) //배열 수 중 가장 큰수와 마지막 수 교환
{
	int last, j;
	int k;
	Array(base, n);//현재 상태 출력

	for (last = n; last > 1; last--)//정렬할 범위를 끝에서 하나씩 축소
	{
		k = 0;
		for (j = 0; j < last; j++)
		{
			k = theLargest(base, last);
			SWAP(base[k], base[last - 1]);//교환
		}

		Array(base, n);//상태 출력
	}
}
int theLargest(int *arr, int last) { //배열 중 가장큰 수의 인덱스를 리턴
	int largest = 1;
	int i;
	for (i = 0; i < last; i++) {
		if (arr[i] > arr[largest]) {
			largest = i;
		}
	}
	return largest;
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