import json
import logging
import os
from typing import Union

logging.basicConfig(
    filename="coding_conventions.logs", level=logging.INFO)

FILE_NAME = "student_data.json"


def add_new_student(student_id: int, name: str,
                    age: int, grade: float) -> None:
    """
    This function adds student information to the json file.

    Parameters
    ----------
    student_id : int
        The unique identifier of the student.
    name : str
        The name of the student.
    age : int
        The age of the student.
    grade : float
        The grade achieved by the student.

    Returns
    -------
    None
        This function does not return anything.
    """
    if not os.path.exists(FILE_NAME):
        logging.info(f"File doesn't exist. Creating a new file: {FILE_NAME}.")
        data = []
        try:
            with open(FILE_NAME, "w", encoding="utf-8") as f:
                data.append({"id": student_id, "name": name,
                            "age": age, "grade": grade})
                json.dump(data, f, indent=4)
                logging.info("Success! Added data in the new file.")
        except Exception as e:
            logging.warning(f"Failure! Failed to add data to the file: {FILE_NAME}")
            print(e)
        finally:
            f.close()
    else:
        try:
            with open(FILE_NAME, "r+", encoding="utf-8") as f:
                data = json.load(f)
                logging.info("File opened successfully")
                f.seek(0)
                data.append({"id": student_id, "name": name,
                             "age": age, "grade": grade})
                json.dump(data, f, indent=4)
                logging.info("Success! Added new student data to the file.")
        except Exception as e:
            logging.warning("Failure! Failed to add new student data to the file")
            print(e)
        finally:
            f.close()


def search_student(key: Union[int, str]) -> str:
    """
    This function searches for a student in the file by their id or name.

    Parameters
    ----------
    key : Union[int, str]
        The key to search for. It can be either an integer (student ID) or a
        string (student name).

    Returns
    -------
    String
        Returns age and grade of the student
    """
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            logging.info("Success! File opened successfully.")
        if isinstance(key, int):
            for dict in data:
                if dict["id"] == key:
                    return f"Age: {dict['age']} and Grage: {dict['grade']}"
            logging.warning(f"Failure! Student with id {key} not found.")
            return None
        elif isinstance(key, str):
            for dict in data:
                if dict["name"] == key:
                    return f"Age: {dict['age']} and Grage: {dict['grade']}"
            logging.warning(f"Failure! Student with name {key} not found.")
            return None
        else:
            logging.warning("Failure! Neither int nor str provided as key.")
            return None
    except Exception as e:
        logging.warning("Failure! Couldn't open the record file.")
        print(e)
    finally:
        f.close()


def update_data(key: Union[int, str], age=None, grade=None) -> None:
    """
    This function updates a student record based on id or name.

    Parameters
    ----------
    key : Union[int, str]
        The key to identify the data. It can be either an integer (student ID)
        or a string (student name).
    age : int, optional
        New age to update
    grade : grade, optional
        New grade to update

    Returns
    -------
    None
        This function doesn't return anything.
    """
    try:
        flag = 0
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            logging.info("Success! File opened successfully.")
        if isinstance(key, int):
            for dict in data:
                if dict["id"] == key:
                    if age:
                        dict["age"] = age
                    if grade:
                        dict["grade"] = grade
                    flag = 1
                    break
            if not flag:
                logging.warning(f"Failure! Student with id {key} not found.")
        elif isinstance(key, str):
            for dict in data:
                if dict["name"] == key:
                    if age:
                        dict["age"] = age
                    if grade:
                        dict["grade"] = grade

                    flag = 1
                    break
            if not flag:
                logging.warning(f"Failure! Student with name {key} not found.")
        try:
            with open(FILE_NAME, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
                logging.info("Success! Updated data successfully.")
        except Exception as e:
            logging.warning("Failure! Failed to update data to the file.")
            print(e)
    except Exception as e:
        logging.warning("Failure! Failed to open file.")
        print(e)


if __name__ == "__main__":
    add_new_student(1, "raj", 20, 3.9)
    add_new_student(2, "rajen", 17, 3.6)
    add_new_student(3, "rajendra", 19, 3.85)
    print(search_student(1))
    print(search_student("rajendra"))
    update_data(1, 21, 4)
    update_data("rajendra", 18, 3.88)
    print(search_student(1))
    print(search_student("rajendra"))
