class Solution {
public:
    int minOperations(vector<string>& logs) {
        int num = 0;
        for(auto& log : logs){
            if(log == "./"){
                continue;
            }
            else if(log == "../"){
                if(num > 0){
                    num = num -1;
                }
            }
            else{
                num = num + 1;
            }
        }
        return num;
    }
};
