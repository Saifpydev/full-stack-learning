function StudnetProfile() {
    let name = "Farid";
    let age = 20;
    let course = "React";
    let college = "Jain College";
    let city = "patna";
    let marks = 1620;

    return (
        <>
        <h1>Student Profile</h1>
        <p>Name: {name}</p>
        <P>Age: {age}</P>
        <p>Course: {course}</p>
        <p>College: {college}</p>
        <P>City: {city}</P>
        <P>marks: {marks}</P>
        <p>Currently I am learning React</p>
        </>
    );
}

export default StudnetProfile;