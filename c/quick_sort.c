#include <stdio.h>
#define SWAP(a,b)  {int t; t = a; a=b; b=t;}//a와 b를 교환

int *origin;
int on;

void QuickSort(int *base, int n);
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
	int p = 0; // 기준 원소를 기억하기 위한 변수
	int left = 0, right = 0; // 기준원소보다 큰 값과 작은 값의 위치를 찾기위한 변수

	if (n <= 1)
	{
		return;
	}

	left = 0;
	right = n;

	while (1) //반복
	{
		for (left++; (left < n) && (base[0] >= base[left]); left++); //전에 끝난 다음부터 시작하기 위해서 left증가, 앞쪽 기준원소보다 큰 값이 나올 때까지 left이동

		for (right--; (right > 0) && (base[0] < base[right]); right--); //뒤쪽에 기준원소보다 작은 값이 나올 때까지 right를 이동

		if (left < right) //left가 right보다 작다면 기준원소보다  작은 값이 큰 값보다 뒤에 있으니까 교환
		{
			SWAP(base[left], base[right]);
			PrintSpace(base - origin);
			Array(base, n);
		}
		else //기준원소를 중심으로 큰 값과 작은 값 분리 완료
		{
			break;
		}
	}

	SWAP(base[0], base[right]); //기준원소를 분리된 작은 값과 큰 값 사이로 보냄
	PrintSpace(base - origin);
	Array(base, n);

	QuickSort(base, right); //기준원소보다 작은 값이 있는 앞쪽 정렬
	QuickSort(base + left, n - left); //기준원소보다 큰 값이 있는 뒤쪽 정렬

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

