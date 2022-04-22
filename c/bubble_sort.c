#include <stdio.h>
#define SWAP(a,b)  {int t; t = a; a=b; b=t;}//a와 b를 교환

void bubbleSort(int *base, int n);

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

	bubbleSort(arr, 10);
	return 0;
}

void Array(int *arr, int n);
void bubbleSort(int *base, int n)
{
	int last, j;
	Array(base, n);//현재 상태 출력

	for (last = n; last > 1; last--)//정렬할 범위를 축소
	{	
		for (j = 1; j < last - 1; j++)//반복
		{
			if (base[j] > base[j + 1])//왼쪽 원소가 더 크면
			{
				SWAP(base[j], base[j + 1]);//교환
				Array(base, n);//상태 출력
			}
		}
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
