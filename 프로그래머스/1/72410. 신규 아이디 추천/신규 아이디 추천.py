def solution(new_id):

    def delete_if_not_alpha_and_num_and_dot_and_hypen(new_id):
        answer = ''

        for ch in new_id:
            if ch.isalnum() or ch in '-_.':
                answer += ch

        return answer

    def delete_if_dot_more_than_two(new_id):
        answer = ''

        for ch in new_id:
            if answer and answer[-1] == '.' and ch == '.':
                continue

            answer += ch

        return answer

    def check_dot_position(new_id):
        if new_id and new_id[0] == ".":
            new_id = new_id[1:]

        if new_id and new_id[-1] == ".":
            new_id = new_id[:-1]

        return new_id

    def check_new_id_is_blank(new_id):
        if len(new_id) == 0:
            new_id = "a"

        return new_id

    def check_new_id_length(new_id):
        if len(new_id) >= 16:
            new_id = new_id[:15]

        return new_id

    def check_length(new_id):
        while len(new_id) < 3:
            new_id += new_id[-1]

        return new_id

    new_id = new_id.lower()
    new_id = delete_if_not_alpha_and_num_and_dot_and_hypen(new_id)
    new_id = delete_if_dot_more_than_two(new_id)
    new_id = check_dot_position(new_id)
    new_id = check_new_id_is_blank(new_id)
    new_id = check_new_id_length(new_id)
    new_id = check_dot_position(new_id)
    new_id = check_length(new_id)

    return new_id