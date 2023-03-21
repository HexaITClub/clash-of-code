#include <stdio.h>
#include <string.h>

char* ltrim(char* st)
{
    while(*st == ' ') st++;
    return st;
}

char* trim(char* str)
{
    str = ltrim(str);
    return str;
}

int32_t valid_nep_name(char* name, int32_t size)
{
    if(size <= 0) return -1;
    int32_t spaces = 0;

    name = trim(name);
    size = strlen(name);

    for(int32_t i = 0; i < size; i++)
    {
        if(name[i] == ' ')
            spaces++;
    }
    if(spaces == 0)
        return -1;
    return spaces + 1;
}

int main(void)
{
    int32_t words = valid_nep_name("Ramesh Poudel", 13);
    printf("%d\n", words);
}
