import { useEffect, useState } from "react";
import { getProjects } from "../api";
import { Link } from "react-router-dom";

export default function ProjectList() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    getProjects().then((res) => setProjects(res.data));
  }, []);

  return (
    <div>
      <h2>Projects</h2>
      <ul>
        {projects.map((p) => (
          <li key={p.id}>
            <h3>{p.name}</h3>
            <p>{p.description}</p>
            <Link to={`/projects/${p.id}/issues`}>View Issues</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
