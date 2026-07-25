import { useState } from "react";

function StudentProfile() {

  const [profile, setProfile] = useState({
    name: "",
    email: "",
    semester: ""
  });

  function handleChange(e) {

    setProfile({

      ...profile,

      [e.target.name]: e.target.value

    });

  }

  return (

    <div>

      <h2>Student Profile</h2>

      <input
        name="name"
        placeholder="Name"
        value={profile.name}
        onChange={handleChange}
      />

      <input
        name="email"
        placeholder="Email"
        value={profile.email}
        onChange={handleChange}
      />

      <input
        name="semester"
        placeholder="Semester"
        value={profile.semester}
        onChange={handleChange}
      />

    </div>

  );
}

export default StudentProfile;