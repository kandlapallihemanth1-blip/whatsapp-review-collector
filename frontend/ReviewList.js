import { useEffect, useState } from "react";
import { fetchReviews } from "./api";

function ReviewList() {
  const [reviews, setReviews] = useState([]);
  useEffect(() => { fetchReviews().then(setReviews); }, []);
  return (
    <table border="1" style={{ width: "100%", marginTop: "20px" }}>
      <thead>
        <tr>
          <th>User</th>
          <th>Product</th>
          <th>Review</th>
          <th>Timestamp</th>
        </tr>
      </thead>
      <tbody>
        {reviews.map(r => (
          <tr key={r.id}>
            <td>{r.user_name}</td>
            <td>{r.product_name}</td>
            <td>{r.product_review}</td>
            <td>{r.created_at}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
export default ReviewList;