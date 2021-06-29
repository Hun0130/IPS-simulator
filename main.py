import systems 
import test
# python main.py로 실행해서 프로그램을 시작시켜주세요

def main():
    # system 객체 생성
    sys = systems.system()
    # finish 입력받을 때 까지 실행
    while (True):
        # 콘솔 그래픽 삭제
        sys.clear()
        # 노드 정보 업데이트
        sys.update()
        # 콘솔 그래픽 출력
        sys.print_grid()
        # command를 받음
        input = sys.get_command()
        # command가 re : system 객체 초기화
        if "re" in input: sys = systems.system()
        # debug : command 입력 안할 시 bug
        if input == "": continue
        # command가 finish : main 프로그램 종료
        if sys.finish(input):
            break
        # command가 add node 20,15 : system의 (20,15) 좌표에 node 추가 
        # node의 기본 채널은 11
        sys.add_node(input)
        # command가 add random 10 : system에 random 좌표의 10개 node 추가
        # node의 기본 채널은 11
        sys.add_random(input)
        # command가 remove node 20,15 : system의 (20, 15) 좌표의 node 제거
        sys.remove_node(input)
        # command가 set channel 20,20 12 : system의 (20, 20) 좌표의 node의 channel을 12로 변경
        sys.set_channel(input)
        # command가 set intfer 11 5 : system의 11채널에 5Mbps의 간섭을 설정 (전체 범위에 일정한 간섭)
        sys.set_interfer(input)
        # command가 add user 1,1 : system에 (1, 1) 좌표에 user 추가
        sys.add_user(input)
        # command가 simul start 20,20 : simulation시작 user를 (20, 20)까지 이동시키면서 위치 추정
        sys.simul_start(input)
        # command가 test 5 : test5를 실행
        sys.test(input)
    return


if __name__ == '__main__':
    main()