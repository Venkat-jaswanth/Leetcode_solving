void display_tokens(){
    if (pd){
        printf("Preprocessor Directives: ");  // Changed from "Preprocessed Directives are"
        for(int i = 0; i < pd; i++)
            printf("%s,", PreprocessedDirectives[i]);  // Removed space before comma
        printf("\n");
    }
    printf("Keywords are: ");
    for(int i = 0; i < kw; i++)
        printf("%s,", Keywords[i]);
    printf("\n");
    printf("Operators are: ");
    for(int i = 0; i < op; i++)
        printf("%s,", Operators[i]);
    printf("\n");
    printf("Identifiers are: ");
    for(int i = 0; i < id; i++)
        printf("%s,", Identifiers[i]);
    printf("\n");
    printf("functions are: ");
    for(int i = 0; i < fn; i++)
        printf("%s,", Functions[i]);
    printf("\n");
    printf("Special symbols are: ");
    for(int i = 0; i < ss; i++)
        printf("%s,", SpecialSymbols[i]);
    printf("\n");
    printf("Constants are: ");
    for(int i = 0; i < cn; i++)
        printf("%s,", Constants[i]);
    printf("\n");
}

void add_function(char arr[32][32], int *count, char *str){
    // Remove trailing whitespace and '(' from function name
    char temp[32];
    strcpy(temp, str);
    int len = strlen(temp);
    while(len > 0 && (temp[len-1] == '(' || temp[len-1] == ' ')) {
        temp[len-1] = '\0';
        len--;
    }
    add_if_not_present(arr, count, temp);
    add_if_not_present(SpecialSymbols, &ss, "(");
}