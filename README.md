## School Event Application 
- Welcome to my school event application!

## Project overview-Feature 
- Create a School
- Update a School
- Delete a School
- Create an Event
- Update an Event
- Delete an Event
- Assign Event to a School
- List Schools
- List Events
- View Events by School
- Exit

## Technologies used
- python 3
- SQL Alchemy
- Alembic

## Installations 
- git clone https://github.com/lgathumbi/event_application
- cd event_application
- code . To open VScode
- Install the necessary Python dependencies 
    1. pipenv install sqlalchemy
    2. pipenv install alembic

## Migrations
- To setup migrations run `alembic init migrations`. We ony run this command once
- Modify alembic.ini `sqlalchemy.url` to the required db i.e test.db
- Modify env.py inside migrations folder and import base model from models file
- To create a migration `alembic revision --autogenerate -m "message"`
- To apply the generatde migration, run `alembic upgrade head`    

## Contributions
- If you have any suggestions or you find issues, feel free to reach out or submit a pull requst.All contributions are welcomed!
1. Fork the project
2. Create a branch
3. Commit your changes
4. Push to branch
5. Open a pull request

## License
- This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
- For any questions or feedback, please reach out to nyawiralornah.gmail.com.
