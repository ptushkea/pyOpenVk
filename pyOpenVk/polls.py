import requests as http
import json

class polls:

    @staticmethod
    def get_poll(client, poll_id, extended=0, fields=''):
        return http.get(f'https://{client["instance"]}/method/Polls.getById?poll_id={poll_id}&extended={extended}&fields={fields}&access_token={client["token"]}').json()

    @staticmethod
    def add_vote(client, poll_id, answers_ids):
        return http.get(f'https://{client["instance"]}/method/Polls.addVote?poll_id={poll_id}&answers_ids={answers_ids}&access_token={client["token"]}').json()

    @staticmethod
    def delete_vote(client, poll_id):
        return http.get(f'https://{client["instance"]}/method/Polls.deleteVote?poll_id={poll_id}&access_token={client["token"]}').json()
