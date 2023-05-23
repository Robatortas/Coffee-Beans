#include <iostream>
#include <filesystem>
#include "Python.h"

void program(const char* path) {
	std::cout << "Running Coffee Beans";
	
	//Py_Initialize();
	//PyRun_SimpleString("import os");
	//PyRun_SimpleString("path = \"python \" + str(os.getcwd()) + \"\\scripts\\Coffee_Beans.py\"");
	//PyRun_SimpleString("print(\"python \" + str(os.getcwd()) + \"\\scripts\\Coffee_Beans.py\")");
	//Py_Finalize();
	std::string command = "python " + std::string(path) + "main.py";
	//const char* command = "python";
}

// COUNTS CHARS ON STRING
int countChars(const char* string) {

	int size = sizeof(string);
	int count = size;
	std::cout << count;
	std::cout << string;
	return count;
}

int main(int argc, char* argv[]) {
	//program(argv[0]);
	countChars("Heyaaaaaaaaaaaaa");
	std::cin.get();
	return 0;
}