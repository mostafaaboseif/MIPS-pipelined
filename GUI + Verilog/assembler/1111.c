#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <sstream>
#include <iterator>
#include <map>
#include <regex>

using namespace std;
vector <string> binary_Instructions;
vector <string> animation;
int instructions_count = 0;
map <string, int> labels;
int labels_count = 0;





bool isDigits(string str); // returns true if str is only digits
void assemble_Line(string line); // calls all the other functions to do the job
string intToBin(short bits, int num); //converts integer to its binary representation
int regToInt(string reg); //converts register name to its decimal value
void make_R(string rs, string rt, string rd, string shamt); //converts the operands to an instruction
void make_I(int op, int rs, int rt, string imm);//converts the operands to an instruction
void make_J(int op, string imm);
void make_Label(string); // converts the label to its line number
string decimalToHex(int dec); //converts integer to its hexdecimal representation


int main() {
	ifstream inFile;
	//opening assembly file
	inFile.open("assemblyCode.txt");
	if (!inFile) {
		cout << "Unable to open file";
		exit(1); // terminate with error
	}

	string line;
	if (inFile.is_open()) {
		while (getline(inFile, line)) {
			replace(line.begin(), line.end(), '\t', ' ');
			//line.erase(remove(line.begin(), line.end(), '\t'), line.end());
			line = regex_replace(line, std::regex("^ +| +$|( ) +"), "$1");
			char codeline[100];
			if (strstr(line.c_str(), ":") != NULL) {
				make_Label(line.c_str());
			}
			strcpy(codeline, line.substr(line.find(":") + 1).c_str());
			if (codeline[0] != '\0' && codeline[0] != '#')assemble_Line(codeline);
		}
		inFile.close();
	}

	//ofstream animation("animation.txt");
	ofstream file("instructionMem.txt");
	//file.open("C:\\Users\\Mohamed Abdullah\\Documents\\Visual Studio 2013\\Projects\\assembley1\\assembley1\\instructionMem.txt");
	//replacing immediate values & Labels
	file << "// memory data file (do not edit the following line - required for mem load use)\n// instance=/atb_all/aa/Imemory\n// format=bin addressradix=h dataradix=b version=1.0 wordsperline=1\n";
	for (int i = 0; i < instructions_count; i++) {
		if (binary_Instructions[i].find("\"") != string::npos) {
			string mywork = binary_Instructions[i];
			string late_conversion = strtok(&mywork[0], "\"\"");
			late_conversion = strtok(NULL, "\"\"");
			binary_Instructions[i].erase(binary_Instructions[i].find("\""), 600);
			//cout << 5;
			if (isDigits(late_conversion)) {
				binary_Instructions[i] += intToBin(16, stoi(late_conversion));
			}
			else if (binary_Instructions[i].substr(0, 6) == "000010" || binary_Instructions[i].substr(0, 6) == "000011") {
				binary_Instructions[i] += intToBin(26, labels[late_conversion]);
			}
			else {
				binary_Instructions[i] += intToBin(16, labels[late_conversion] - (i + 1));
			}
		}
		//adding the address in hexdecimal to the instruction
		binary_Instructions[i] = string(decimalToHex(instructions_count).size() - decimalToHex(i).size(), ' ') + decimalToHex(i) + binary_Instructions[i];
		file << binary_Instructions[i] << endl;
	}
	binary_Instructions.push_back(decimalToHex(instructions_count) + string(32, '1'));
	file << binary_Instructions.back() << "\n";

	file.close();
	ofstream flags("animation.txt");
	for (int i = 0; i < animation.size(); i++) {
		flags << animation[i] << endl;
	}
	cout << "Oleeee" << endl;
	return 0;
}


bool isDigits(string str) {
	return str.find_first_not_of("-0123456789") == string::npos;
}
string intToBin(short bits, int num) {
	// bits is the lenght of the binary
	// num is the number to be converted to binary
	unsigned int posnum = abs(num);
	string binary = "";
	for (int i = bits - 1; i >= 0; i--) {
		if (posnum & (1 << i))binary += "1";
		else binary += "0";
	}
	if (num < 0) {
		int flag = 0;
		for (int i = binary.size() - 1; i >= 0; i--) {
			if (flag == 1 && binary[i] == '1')binary[i] = '0';
			else if (flag == 1) binary[i] = '1';
			if (binary[i] == '1')flag = 1;
		}
	}
	return binary;
}
int regToInt(string reg) {
	if (reg == "$zero")return 0;
	else if (reg == "$at")return 1;
	else if (reg[1] == 'v')return 2 + reg[2] - '0';
	else if (reg[1] == 'a')return 4 + reg[2] - '0';
	else if (reg[1] == 't' && reg[2] - '0' <= 7)return 8 + reg[2] - '0';
	else if (reg == "$sp")return 29;
	else if (reg[1] == 's')return 16 + reg[2] - '0';
	else if (reg[1] == 't')return 24 + reg[2] - '0';
	else if (reg[1] == 'k')return 26 + reg[2] - '0';
	else if (reg == "$gp")return 28;
	else if (reg == "$fp")return 30;
	else if (reg == "$ra")return 31;
}
void make_R(int op, int rs, int rt, int rd, int shamt, int funct) {
	string instruction = "";
	instruction += intToBin(6, op);
	instruction += intToBin(5, rs);
	instruction += intToBin(5, rt);
	instruction += intToBin(5, rd);
	instruction += intToBin(5, shamt);
	instruction += intToBin(6, funct);
	binary_Instructions.push_back(instruction);
	instructions_count++;
}
void make_Label(string label) {
	label = label.substr(0, label.find(":"));
	label = regex_replace(label, std::regex("^ +| +$|( ) +"), "$1");  //remove leading spaces , extra spaces , trailing spaces
	labels.insert(make_pair(label, instructions_count));
}
void make_I(int op, int rs, int rt, string imm) {
	string instruction = "";
	instruction += intToBin(6, op);
	instruction += intToBin(5, rs);
	instruction += intToBin(5, rt);
	instruction += "\"" + imm + "\"";
	//instruction += intToBin(16, imm);
	binary_Instructions.push_back(instruction);
	instructions_count++;
}
void make_J(int op, string imm) {
	string instruction = "";
	instruction += intToBin(6, op);
	instruction += "\"" + imm + "\"";
	//instruction += intToBin(16, imm);
	binary_Instructions.push_back(instruction);
	instructions_count++;
}
string decimalToHex(int dec) {
	std::stringstream ss;
	ss << std::hex << dec; // int decimal_value
	std::string res(ss.str());
	return "@" + res + " ";
}

void assemble_Line(string line) {
	vector <string> result(4, "");
	int count = 0;
	int start = 0;
	int flag = 1;
	line = regex_replace(line, std::regex("^ +| +$|( ) +"), "$1"); //remove leading spaces , extra spaces , trailing spaces

	//parsing the line (instruction) to parts (registers & values )
	for (unsigned int i = 0; i <= line.size(); i++) {
		if ((line[i] == ' ' || line[i] == ',' || line[i] == '\0') && flag == 1) {
			result[count++] = line.substr(start, i - start);
			flag = 0;
		}
		if (line.size() != i && (line[i] == ' ' || line[i] == ',' || line[i] == '\0') && (line[i + 1] != ' ' && line[i + 1] != ',')) {
			start = i + 1;
			flag = 1;
		}
	}

	string first = result[0], second = result[1], third = result[2], fourth = result[3];

	// supporting registers written as Decimal values feature
	int two, three, four;
	if (isDigits(second))two = stoi(second);
	else two = regToInt(second);
	if (isDigits(third) && third != "")three = stoi(third);
	else if (third != "") three = regToInt(third);
	if (isDigits(fourth) && fourth != "")four = stoi(fourth);
	else if (fourth != "") four = regToInt(fourth);

	if (first == "add") {
		make_R(0, three, four, two, 0, 32);
		animation.push_back("R");
	}
	else if (first == "and") {
		make_R(0, three, four, two, 0, 36);
		animation.push_back("R");

	}
	else if (first == "jr") {
		make_R(0, two, 0, 0, 0, 8);
		animation.push_back("JR");
	}
	else if (first == "nor") {
		make_R(0, three, four, two, 0, 39);
		animation.push_back("R");
	}
	else if (first == "or") {
		make_R(0, three, four, two, 0, 37);
		animation.push_back("R");
	}
	else if (first == "sll") {
		make_R(0, 0, three, two, four, 0);
		animation.push_back("R");

	}
	else if (first == "slt") {
		make_R(0, three, four, two, 0, 42);
		animation.push_back("R");
	}
	else if (first == "sra") {
		make_R(0, 0, three, two, four, 3);
		animation.push_back("R");
	}
	else if (first == "srl") {
		make_R(0, 0, three, two, four, 2);
		animation.push_back("R");
	}
	else if (first == "sub") {
		make_R(0, three, four, two, 0, 34);
		animation.push_back("R");
	}
	else if (first == "xor") {
		make_R(0, three, four, two, 0, 38);
		animation.push_back("R");
	}
	else if (first == "addi") {
		make_I(8, three, two, fourth);
		animation.push_back("R");
	}
	else if (first == "andi") {
		make_I(12, three, two, fourth);
		animation.push_back("R");
	}
	else if (first == "beq") {
		make_I(4, two, three, fourth);
		animation.push_back("B");
	}
	else if (first == "bne") {
		make_I(5, two, three, fourth);
		animation.push_back("B");
	}
	else if (first == "lw") {
		string offset = strtok(&(third[0]), "()");
		string rs = strtok(NULL, "()");
		if (isDigits(rs)) make_I(35, stoi(rs), regToInt(second), offset);
		else make_I(35, regToInt(rs), regToInt(second), offset);
		animation.push_back("LW");
	}
	else if (first == "ori") {
		make_I(13, three, two, fourth);
		animation.push_back("R");
	}
	else if (first == "sw") {
		string offset = strtok(&(third[0]), "()");
		string rs = strtok(NULL, "()");
		if (isDigits(rs)) make_I(43, stoi(rs), regToInt(second), offset);
		else make_I(43, regToInt(rs), regToInt(second), offset);
		animation.push_back("SW");
	}
	else if (first == "xori") {
		make_I(14, three, two, fourth);
		animation.push_back("R");
	}
	else if (first == "j") {
		make_J(2, second);
		animation.push_back("J");
	}
	else if (first == "jal") {
		make_J(3, second);
		animation.push_back("JAL");
	}

}
