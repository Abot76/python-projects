#include <random>
#include <iostream>
using namespace std;

int comp_choice;
int user_choice;


void Draw() {
    cout << "Draw! PLay again." << endl;
}

void User_Won() {
    cout << "You won!" << endl;
}

void Comp_Won() {
    cout << "You lost! Try again." << endl;
}


int main () {
    while (true) {
        int comp_choice = rand() % 4;

        cout << "[1] rock" << endl << "[2] paper" << endl << "[3] scisors" << endl;
        cin >> user_choice;

        if (user_choice == comp_choice) {
            Draw();
        }


        if (user_choice == 1) {
            if (comp_choice == 2) {
                Comp_Won();
            }

            else if (comp_choice == 3) {
                User_Won();
                break;
            }
        }
        else if (user_choice == 2) {
            if (comp_choice == 1) {
                User_Won();
                break;
            }

            else if (comp_choice == 3) {
                Comp_Won();
            }
        }
        else if (user_choice == 3) {
            if (comp_choice == 1) {
                Comp_Won();
            }

            else if (comp_choice == 2) {
                User_Won();
                break;
            }
        }

    }

    return 0;
}