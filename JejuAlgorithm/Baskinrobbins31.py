'''

int num;
int total = 0;
int count = 0;
int player_num;
int list = []
print("숫자를 몇개 입력하시겠습니까?");
scanf("%d", num);  // 3

if ( num > 3 || num < 1 ) {
    printf("1~3개 중에서 입력해주세요");
}
else if ( (total+count) > 31 ) {
 break;
}

else {
    print("당신이 입력한 숫자 : ");
    for( i = 0; i < num; i ++ ){
        scanf("%d", player_num );
        list[i] = player_num  // 1,2,3
        count++;
    }
    if( (total+count) == 31 ) {
        printf("패배");
        break;
    }


}

int num_a;

        if(turn == i){  // i번째 사용자 턴일 경우

                if(num > 0 && num < 4) {
                        fprintf(stderr, "\033[33m");
                        printf("\n\t ------------------------------------------------------ \n");
                        printf("\t\t %s 가 부른 숫자 :  ",player);
                        for( present=total+1; present<=total+num; present++){
                                printf(" %d", present);
                                if(present!=total+num)
                                        printf(",");
                        }
                        puts("");
                        total += num;
                        printf("현재까지 3 1 게임의 마지막 수 => %d 입니다\n", total);
                        if(total >= 31) {
                                for(k = 0 ; k<2; k++){
                                        if(i==k)
                                                send(clisock_list[k],LOSE,strlen(LOSE), 0);
                                        else
                                                send(clisock_list[k],WIN,strlen(WIN), 0);
                                }
                                printf("최종 : %s가 졌습니다.\n",player);
                                is_GameStart = 0;
                        }
                        else{
                                sprintf(inputBuf, "%s : %d 입력 현재 숫자[%d]\n", player, num, total);
                                for(k = 0; k<2; k++)
                                        if(i==k){
                                                sprintf(resultBuf, "%s \n 차례를 기다리세요....", inputBuf);
                                                send(clisock_list[k], resultBuf,strlen(resultBuf), 0);
                                        }
                                        else{
                                                sprintf(resultBuf, "%s \n 당신의 차례입니다.....:)",inputBuf);
                                                send(clisock_list[k], resultBuf, strlen(resultBuf),0);
                                        }
                                        turn = (i+1)%2;
                        }
                }
                else{
                        sprintf(input_error, "%s가 %s\n", player,"잘못입력");
                        for(j = 0; j < num_chat; j++) {
                                send(clisock_list[j], input_error, strlen(input_error),0);
                        }
                }
        }
        else{
                send(clisock_list[i], WRONG_TURN_STRING, strlen(WRONG_TURN_STRING), 0);
        }






'''
