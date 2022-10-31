from mean_elapsed_time import mean

import io
import math
import pytest


def test_should_print_sliding_mean_elapsed_time(mocker):
    expected_msg = 'Mean execution time of update_perf_counter over 3 runs is'

    start_end_3mean = [
        (0.0, 1.1, None),
        (1.2, 1.5, None),
        (1.8, 2.6, 2.2 / 3),
        (2.9, 3.5, 1.7 / 3),
        (3.5, 4.1, 2.0 / 3),
        (4.2, 7.9, 4.9 / 3),
    ]

    @mean(3)
    def update_perf_counter(new_perf_counter_value):
        mocker.patch('time.perf_counter', return_value=new_perf_counter_value)

    for i, (start, end, sliding_mean) in enumerate(start_end_3mean):
        stdout = mocker.patch('sys.stdout', new_callable=io.StringIO)
        mocker.patch('time.perf_counter', return_value=start)
        update_perf_counter(end)

        if sliding_mean is None:
            assert stdout.getvalue() == ''
            continue

        msg, measure = stdout.getvalue().rsplit(maxsplit=1)
        assert msg == expected_msg
        assert math.isclose(float(measure), sliding_mean)


@pytest.mark.parametrize('wndsize', (1, 2, 3, 5, 10))
def test_should_work_with_various_window_sizes(mocker, wndsize):
    @mean(wndsize)
    def func():
        pass

    for i in range(wndsize - 1):
        stdout = mocker.patch('sys.stdout', new_callable=io.StringIO)
        func()
        assert stdout.getvalue() == ''

    stdout = mocker.patch('sys.stdout', new_callable=io.StringIO)
    func()
    assert stdout.getvalue().startswith(
        f'Mean execution time of func over {wndsize} runs is '
    )


def test_should_work_with_various_func_args():
    @mean(1)
    def func(*args, **kwargs):
        assert args == ('a', 'b', 'c')
        assert kwargs == {'x': 1, 'y': 2, 'z': 3}

    func('a', 'b', 'c', x=1, y=2, z=3)
