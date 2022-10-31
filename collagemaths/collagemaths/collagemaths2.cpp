#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h> 
#include <pthread.h>
#include <iostream>
#include <filesystem>

using namespace std;
namespace fs = std::filesystem;
void *  best_patch_finder(void  *number);

struct args {
    char* name;
    int age;
};

vector<vector<string>> patches_matrix;
vector<vector<string>> target_patch_matrix;

string** answer_data = (string**)calloc(72000, sizeof( "C:\\Users\\Zachary\\Desktop\\C collage\\Editcolorofimage\\cut_and_downscaled_money_patches.csv") * 4);


int number_of_threads = 2;

int main()
{
	string fname = "C:\\Users\\Zachary\\Desktop\\C collage\\Editcolorofimage\\cut_and_downscaled_money_patches.csv";
	
	vector<string> row;
	string line, word;
	fstream file(fname, ios::in);
	if (file.is_open())
	{
		while (getline(file, line))
		{
			row.clear();

			stringstream str(line);

			while (getline(str, word, ','))
				row.push_back(word);
			target_patch_matrix.push_back(row);
		}
	}
	else
		cout << "Could not open the file\n";

	string fname2 = "C:\\Users\\Zachary\\Desktop\\C collage\\Editcolorofimage\\downscaled_patches_data.csv";
	
	vector<string> row2;
	string line2, word2;
	fstream file2(fname2, ios::in);
	if (file2.is_open())
	{
		while (getline(file2, line2))
		{
			row2.clear();

			stringstream str(line2);

			while (getline(str, word2, ','))
				row2.push_back(word2);
			patches_matrix.push_back(row2);
		}
	}
	else
		cout << "Could not open the file\n";



	int target;
	int best_score = 1000000;
	string best_patch = "";
	std::ofstream myfile;
	
	int sum = 0;
	int x;
	ifstream inFile;

	inFile.open("C:\\Users\\Zachary\\Desktop\\C collage\\Editcolorofimage\\num_patches_height.txt");
	if (!inFile) {
		cout << "Unable to open file";
		exit(1); // terminate with error
	}

	while (inFile >> x) {
		sum = sum + x;
	}

	inFile.close();

	myfile.open("C:\\Users\\Zachary\\Desktop\\C collage\\Editcolorofimage\\answer.csv");

	int temp;
	int temp2;
	int temp3;
	int temp4;
	int temp5;
	int temp6 = 0;
	int temp7;

	struct args *Allen = (struct args *)malloc(sizeof(struct args));
    char allen[] = "Allen";
    Allen->name = allen;
    Allen->age = 0;

	struct args *Allen2 = (struct args *)malloc(sizeof(struct args));
    char allen2[] = "Allen";
    Allen2->name = allen2;
    Allen2->age = 1;


	pthread_t first;
    pthread_t second;
	pthread_create(&first, NULL, best_patch_finder,  (void *)Allen);
	pthread_create(&second, NULL, best_patch_finder, (void *)Allen2);
	pthread_join(first, NULL);
	pthread_join(second, NULL);

	int z;
	z = 0;
	

	for (int i = 0; i < target_patch_matrix.size(); i++){
		
		string x_coords   = answer_data[i][0];
		string y_coords   = answer_data[i][1];
		string best_patch = answer_data[i][2];
		myfile << x_coords + "," + y_coords + "," + best_patch  +"\n";
		auto p = std::to_string(temp6);
		temp6 = temp6 + 1;
		z++;
	}
	
	myfile.close();

	return 0;
}



void *  best_patch_finder(void  *number){

	int size_of_first_half  = target_patch_matrix.size()/number_of_threads;
	int size_of_second_half = target_patch_matrix.size()/ number_of_threads + target_patch_matrix.size() % number_of_threads; 
	int start;
	int end;

	int thread = ((struct args*)number) -> age;
	printf("thread %d\n", thread);


	if (thread == 0){start= 0; end = size_of_first_half;}
	else {start= size_of_first_half; end = size_of_first_half + size_of_second_half;}

	int target;
	int temp5;
	int temp4;
	int sum;
	string best_patch;
	int best_score;
	int v = target_patch_matrix.size();

	

	for (int z = start; z < end ; z++) {
		best_score = 1000000;
		for (int i = 0; i < patches_matrix.size(); i++)
		{
			if (patches_matrix[i][1] == "square"){
				target = 0;
				for (int j = 3; j < 64*3 + 2; j++) {
					target = target + abs(stoi(patches_matrix[i][j]) - stoi(target_patch_matrix[z][j]));
				}

				if (target < best_score) {
					best_score = target;
					best_patch = patches_matrix[i][0];
				}
			}
			if (patches_matrix[i][1] == "landscape") {
				target = 0;
				temp4 = z + sum;
				for (int j = 3; j < 64 * 3 + 2; j++) {
					target = target + abs(stoi(patches_matrix[i][j]) - stoi(target_patch_matrix[z][j]));
				}
				
				if (temp4 < target_patch_matrix.size()) {
					for (int j = 2; j < 64 * 3 + 2; j++) {
						temp5 = j + 64 * 3;
						target = target + abs(stoi(patches_matrix[i][temp5]) - stoi(target_patch_matrix[temp4][j]));
					}
				}
				else {
					target = target + 100000;

				}
				target = target / 2;
				if (target < best_score) {
					best_score = target;
					best_patch = patches_matrix[i][0];
				}

			}
			if (patches_matrix[i][1] == "portrait") {
				target = 0;
				for (int j = 3; j < 64 * 3 + 2; j++) {
					target = target + abs(stoi(patches_matrix[i][j]) - stoi(target_patch_matrix[z][j]));
				}
				temp4 = z + 1;
				if (temp4 < target_patch_matrix.size()) {
					for (int j = 2; j < 64 * 3 + 2; j++) {
						temp5 = j + 64 * 3;
						target = target + abs(stoi(patches_matrix[i][temp5]) - stoi(target_patch_matrix[temp4][j]));
					}
				}
				else {
					target = target + 10000000;
				}
				target = target / 2;
				if (target < best_score) {
					best_score = target;
					best_patch = patches_matrix[i][0];
				}
			}
		}


		cout << z;
		cout << "/";
		auto s = std::to_string(target_patch_matrix.size());
		cout << s + " Scorez:";
		cout << " " + to_string(best_score) + " ";
		cout << best_patch;
		cout << "\n";
		answer_data[z] = new string[4];
		answer_data[z][0] = target_patch_matrix[z][0];
		answer_data[z][1] = target_patch_matrix[z][1];
		answer_data[z][2] = best_patch;
		answer_data[z][3] = to_string(best_score);
		}
}