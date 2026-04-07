import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { getProjectIssues, createIssue, updateIssueStatus } from "../api";

export default function IssueList() {
  const { projectId } = useParams();
  const [issues, setIssues] = useState([]);
  const [newIssue, setNewIssue] = useState({ title: "", description: "" });

  useEffect(() => {
    getProjectIssues(projectId).then((res) => setIssues(res.data));
  }, [projectId]);

  const handleCreate = () => {
    createIssue({ ...newIssue, project_id: parseInt(projectId) }).then(
      (res) => {
        setIssues([...issues, res.data]);
        setNewIssue({ title: "", description: "" });
      },
    );
  };

  const handleStatusChange = (id, status) => {
    updateIssueStatus(id, status).then((res) => {
      setIssues(issues.map((i) => (i.id === id ? res.data : i)));
    });
  };

  return (
    <div>
      <h2>Issues for Project {projectId}</h2>
      <ul>
        {issues.map((issue) => (
          <li key={issue.id}>
            <Link to={`/issues/${issue.id}`}>{issue.title}</Link> -{" "}
            {issue.status} ({issue.priority})
            <button onClick={() => handleStatusChange(issue.id, "in_progress")}>
              Start
            </button>
            <button onClick={() => handleStatusChange(issue.id, "closed")}>
              Close
            </button>
          </li>
        ))}
      </ul>
      <h3>Create New Issue</h3>
      <input
        value={newIssue.title}
        onChange={(e) => setNewIssue({ ...newIssue, title: e.target.value })}
        placeholder="Title"
      />
      <input
        value={newIssue.description}
        onChange={(e) =>
          setNewIssue({ ...newIssue, description: e.target.value })
        }
        placeholder="Description"
      />
      <button onClick={handleCreate}>Create</button>
    </div>
  );
}
