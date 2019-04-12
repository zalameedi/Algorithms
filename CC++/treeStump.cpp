#include<iostream>
#include<vector>
#include<sys/socket.h>
#include<unordered_map>
#include<string>
#include<cstdlib>
#include<numeric>

void drawTree(int height);

int main()
{
    int height=0;
    std::cout<<"How tall is the tree? ";
    std::cin >> height;
    drawTree(height);
    return 0;
}

void drawTree(int height)
{
    std::string blank;
    std::string hashes="#";
    while (height != 0)
    {
        for(int whiteSpace = 0; whiteSpace < height; whiteSpace++)
        {
            blank.append(" ");
        }
        std::cout<<blank<<hashes<<"\n";
        hashes.append("##");
        height -= 1;
        blank="";
    }
}