int getMoneySpent(int keyboards_count, int* keyboards, int drives_count, int* drives, int b) {
    int i,j,total=99999,sum=0;
    for(i=0;i<keyboards_count;i++){
        for (j=0; j<drives_count; j++) {
            if(total>keyboards[i]+drives[j])
                total=keyboards[i]+drives[j];
        }
    }
    if(total>b || total==99999)
        return -1;
    else{
        for(i=0;i<keyboards_count;i++){
            for (j=0; j<drives_count; j++) {
                sum=keyboards[i]+drives[j];
                if(sum<=b && sum>=total)
                    total=sum;
            }
        }
        return total;
    }
}
