#include "HeaderNIZ1.h"


//void main() 
//{
//
//	TestFunction(MUL_8);
//
//
//	int w = getchar();
//
//}


int main(int argc, char* argv[]) {
	if (argc <= 1) {
		
		return -1;
	}
	else {
		for (int i = 0; argv[i] != NULL; i++) {
			
			printf("%s\n", argv[i]);
		}
	}
	return 0;
}