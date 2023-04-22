## Using the News Proposal Table

This resource allows you to work with a table of proposals. To read and add new entries, you can use the following URL: `http://127.0.0.1:8000/news/api/v1/newslist/`.

To gain access, follow these steps:

1. Register a user by sending a POST request with the `username`, `password`, and `email` fields to `http://127.0.0.1:8000/news/api/v1/auth/users/`. If the registration is successful, you will receive a response in the form of a JSON file containing the `email`, `id`, and `username` fields.

2. Obtain a token by sending a POST request with the `username` and `password` fields to `http://127.0.0.1:8000/news/auth/token/login/`. If the request is successful, you will receive a response in the form of a JSON file containing the `auth_token` field.

3. Now you can view and add new entries at `http://127.0.0.1:8000/news/api/v1/newslist/`. To do this, include the received token in the "Headers" section of the GET or POST request with the "Authorization" key. The value should be in the format `Token <received token>`.

With a GET request, you will receive a response containing a collection of records in JSON format with the following fields: `channel_url`, `channel_name`, `channel_desc`, `time_create`, `time_update`, and `slug`.

To add new records, send a POST request with the `channel_name`, `channel_url`, and `channel_desс` fields.

To edit or delete your entry, use the following URLs:
- `http://127.0.0.1:8000/news/api/v1/newslist/<slug:slug>/`
- `http://127.0.0.1:8000/news/api/v1/newslist/delete/<slug:slug>/`

Note: To edit or delete an entry, you do not need to provide the token. It is sufficient to be authorized by login and password. Otherwise, you will only be able to read the entry.
