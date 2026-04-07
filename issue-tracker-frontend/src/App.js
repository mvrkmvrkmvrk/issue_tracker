import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ProjectList from "./pages/ProjectList";
import IssueList from "./pages/IssueList";
import IssueDetail from "./pages/IssueDetail";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ProjectList />} />
        <Route path="/projects/:projectId/issues" element={<IssueList />} />
        <Route path="/issues/:issueId" element={<IssueDetail />} />
      </Routes>
    </Router>
  );
}

export default App;
