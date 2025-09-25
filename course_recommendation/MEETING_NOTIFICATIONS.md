# Meeting Notification System

## Overview
A comprehensive meeting notification system with real-time Socket.IO notifications and PostgreSQL database storage. This system handles meeting scheduling, reminders, cancellations, and can be extended for message notifications.

## Database Table: `meeting_notifications`

```sql
CREATE TABLE meeting_notifications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    mentor_id INTEGER NOT NULL,
    schedule_id INTEGER,
    notification_type VARCHAR(50) NOT NULL,
    title VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    meeting_datetime TIMESTAMP,
    meeting_link VARCHAR(500),
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    read_at TIMESTAMP,
    notification_data JSON
);
```

## Socket.IO Events

### Client to Server Events

1. **`join_meeting_room`** - Join a user to their meeting notification room
   ```javascript
   socket.emit('join_meeting_room', {
       user_id: 123,
       user_type: 'user' // or 'mentor'
   });
   ```

2. **`get_meeting_notifications`** - Get all meeting notifications for a user
   ```javascript
   socket.emit('get_meeting_notifications', {
       user_id: 123
   });
   ```

3. **`mark_notification_read`** - Mark a notification as read
   ```javascript
   socket.emit('mark_notification_read', {
       notification_id: 456,
       user_id: 123
   });
   ```

### Server to Client Events

1. **`new_meeting_notification`** - New notification received
   ```javascript
   socket.on('new_meeting_notification', (notification) => {
       console.log('New notification:', notification);
   });
   ```

2. **`meeting_notifications`** - List of notifications
   ```javascript
   socket.on('meeting_notifications', (data) => {
       console.log('Notifications:', data.notifications);
   });
   ```

3. **`notification_marked_read`** - Confirmation of read status
   ```javascript
   socket.on('notification_marked_read', (data) => {
       console.log('Notification marked as read:', data);
   });
   ```

## API Endpoints

### 1. Get Meeting Notifications
```
GET /api/meeting-notifications
```
**Query Parameters:**
- `limit` (optional): Number of notifications to return (default: 50)
- `offset` (optional): Number of notifications to skip (default: 0)
- `unread_only` (optional): Return only unread notifications (default: false)

**Response:**
```json
{
    "notifications": [
        {
            "id": 1,
            "mentor_id": 123,
            "schedule_id": 456,
            "notification_type": "meeting_scheduled",
            "title": "Meeting Scheduled",
            "message": "Your meeting with John Doe has been scheduled...",
            "meeting_datetime": "2024-01-15T10:00:00",
            "meeting_link": "https://meet.google.com/abc-def-ghi",
            "is_read": false,
            "created_at": "2024-01-10T09:00:00",
            "read_at": null,
            "notification_data": {
                "mentor_name": "John Doe",
                "duration": 60
            }
        }
    ]
}
```

### 2. Mark Notification as Read
```
PUT /api/meeting-notifications/{notification_id}/read
```

### 3. Mark All Notifications as Read
```
PUT /api/meeting-notifications/mark-all-read
```

### 4. Get Unread Count
```
GET /api/meeting-notifications/unread-count
```

### 5. Create Meeting Notification
```
POST /api/meeting-notifications
```
**Request Body:**
```json
{
    "user_id": 123,
    "mentor_id": 456,
    "schedule_id": 789,
    "notification_type": "meeting_scheduled",
    "title": "Meeting Scheduled",
    "message": "Your meeting has been scheduled...",
    "meeting_datetime": "2024-01-15T10:00:00",
    "meeting_link": "https://meet.google.com/abc-def-ghi",
    "notification_data": {
        "mentor_name": "John Doe",
        "duration": 60
    }
}
```

### 6. Send Meeting Reminder
```
POST /api/meeting-notifications/reminder
```
**Request Body:**
```json
{
    "schedule_id": 789
}
```

### 7. Send Meeting Cancellation
```
POST /api/meeting-notifications/cancel
```
**Request Body:**
```json
{
    "schedule_id": 789,
    "reason": "Emergency came up"
}
```

### 8. Get Upcoming Meetings
```
GET /api/meeting-notifications/upcoming
```

## Notification Types

1. **`meeting_scheduled`** - When a new meeting is scheduled
2. **`meeting_reminder`** - Reminder before a meeting
3. **`meeting_cancelled`** - When a meeting is cancelled
4. **`message`** - For future message notifications

## Integration with Existing Schedule System

The notification system is automatically integrated with:
- `/api/schedule` - Regular meeting scheduling
- `/api/trial_schedule` - Trial meeting scheduling

When a meeting is scheduled, notifications are automatically sent to both the user and mentor.

## Helper Function

### `send_meeting_notification()`
A helper function that creates a notification record and sends real-time Socket.IO notification:

```python
send_meeting_notification(
    user_id=123,
    mentor_id=456,
    notification_type='meeting_scheduled',
    title='Meeting Scheduled',
    message='Your meeting has been scheduled...',
    schedule_id=789,
    meeting_datetime=datetime_obj,
    meeting_link='https://meet.google.com/abc-def-ghi',
    notification_data={'mentor_name': 'John Doe', 'duration': 60}
)
```

## Future Extensions

The system is designed to be extensible for:
1. **Message Notifications** - Use the same table and Socket.IO events for chat messages
2. **Push Notifications** - Integrate with mobile push notification services
3. **Email Notifications** - Send email notifications alongside real-time ones
4. **SMS Notifications** - Send SMS for critical notifications

## Usage Examples

### Frontend Integration

```javascript
// Connect to Socket.IO
const socket = io('http://localhost:5000');

// Join meeting notification room
socket.emit('join_meeting_room', {
    user_id: currentUserId,
    user_type: 'user'
});

// Listen for new notifications
socket.on('new_meeting_notification', (notification) => {
    // Show notification in UI
    showNotification(notification);
});

// Get all notifications
socket.emit('get_meeting_notifications', {
    user_id: currentUserId
});

// Mark notification as read
socket.emit('mark_notification_read', {
    notification_id: notificationId,
    user_id: currentUserId
});
```

### Backend Integration

```python
# Send a custom notification
send_meeting_notification(
    user_id=user.id,
    mentor_id=mentor.id,
    notification_type='meeting_reminder',
    title='Meeting Reminder',
    message=f'Your meeting is in 30 minutes',
    schedule_id=schedule.id,
    meeting_datetime=schedule.start_datetime,
    meeting_link=schedule.link
)
```

## Security

- All API endpoints require JWT authentication
- Users can only access their own notifications
- Socket.IO rooms are user-specific to prevent unauthorized access
- Input validation on all endpoints

## Error Handling

- Graceful error handling in all Socket.IO events
- Database transaction rollback on errors
- Comprehensive error messages in API responses
- Logging for debugging and monitoring
