import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getIssue, getComments, addComment } from "../api";

export default function IssueDetail() {
  const { issueId } = useParams();
  const [issue, setIssue] = useState(null);
  const [comments, setComments] = useState([]);
  const [newComment, setNewComment] = useState("");

  useEffect(() => {
    getIssue(issueId).then((res) => setIssue(res.data));
    getComments(issueId).then((res) => setComments(res.data));
  }, [issueId]);

  const handleAddComment = () => {
    addComment(issueId, { user_id: 1, message: newComment }).then((res) => {
      setComments([...comments, res.data]);
      setNewComment("");
    });
  };

  if (!issue) return <div>Loading...</div>;

  return (
    <div>
      <h2>{issue.title}</h2>
      <p>{issue.description}</p>
      <p>Status: {issue.status}</p>
      <p>Priority: {issue.priority}</p>
      <p>Assigned to: {issue.assigned_to}</p>

      <h3>Comments</h3>
      <ul>
        {comments.map((c) => (
          <li key={c.id}>
            {c.message} (User {c.user_id})
          </li>
        ))}
      </ul>
      <input
        value={newComment}
        onChange={(e) => setNewComment(e.target.value)}
        placeholder="Add a comment"
      />
      <button onClick={handleAddComment}>Submit</button>
    </div>
  );
}
