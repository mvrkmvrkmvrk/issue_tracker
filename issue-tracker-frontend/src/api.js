import axios from "axios";

const API_BASE = "http://localhost:8000"; // FastAPI backend

export const getProjects = () => axios.get(`${API_BASE}/projects/`);
export const getProjectIssues = (projectId) =>
  axios.get(`${API_BASE}/projects/${projectId}/issues`);
export const createIssue = (data) => axios.post(`${API_BASE}/issues`, data);
export const updateIssueStatus = (issueId, status) =>
  axios.put(`${API_BASE}/issues/${issueId}/status`, { status });
export const assignIssue = (issueId, userId) =>
  axios.put(`${API_BASE}/issues/${issueId}/assign`, { user_id: userId });
export const getIssue = (issueId) => axios.get(`${API_BASE}/issues/${issueId}`);
export const getComments = (issueId) =>
  axios.get(`${API_BASE}/issues/${issueId}/comments`);
export const addComment = (issueId, data) =>
  axios.post(`${API_BASE}/issues/${issueId}/comments`, data);
