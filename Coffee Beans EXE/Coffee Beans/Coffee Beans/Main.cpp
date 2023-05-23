#include <iostream>
#include <filesystem>
#include <Windows.h>

void program() {
	std::cout << "Running Coffee Beans";
	std::filesystem::path path = std::filesystem::current_path();
	std::string command = "python \"" + path.string() + "\\internal\\coffee_beans.py\"";
	std::cout << "\n\nWILL BE RUNNING APPLICATION AT: " << command << "\n\n";
	::ShowWindow(::GetConsoleWindow(), SW_HIDE);
	std::system(std::string(command).c_str());
	return;
}

int main() {
	program();
	return 0;
}