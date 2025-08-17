# Summary

AWS will block connections from the internet by default, especially in ports other than 80. Rules will needed to be added to Security Groups to expose the required ports.

## Security Group Rules

|            |           |               |     |
| ---------- | --------- | ------------- | --- |
| Type       | Port      | Allowed Hosts |     |
| Custom TCP | Port 8000 | 0.0.0.0/0     |     |
| Custom TCP | Port 5173 | 0.0.0.0/0     |     |