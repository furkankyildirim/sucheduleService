# SUchedule Service

A Node.js service that provides schedule data for Sabancı University students. This service is deployed on AWS Lambda and automatically updates its data from the [SUchedule](https://github.com/aburakayaz/suchedule) repository.

## Features

- Provides course schedule data via REST API
- Automatic daily updates from the source repository
- Serverless deployment on AWS Lambda
- Continuous Integration/Continuous Deployment with GitHub Actions

## API Endpoints

### GET /
Health check endpoint that returns service name.

Response:
```json
{
    "name": "SUchedule"
}
```

### GET /version
Returns current version information.

Response:
```json
{
    "name": "SUchedule",
    "term": "202401",
    "version": 39,
    "start-date": "2024-09-23",
    "end-date": "2024-12-31"
}
```

### GET /data
Returns the complete course schedule data.

## Local Development

1. Install dependencies:
```bash
npm install
```

2. Run the service locally:
```bash
npm start
```

The service will be available at `http://localhost:3000`

## Deployment

The service is automatically deployed to AWS Lambda when changes are pushed to the master branch. The deployment process includes:

1. Creating a deployment package
2. Updating the Lambda function
3. Publishing a new version
4. Updating the production alias
5. Verifying the deployment

### Manual Deployment

To deploy manually, trigger the "Deploy to AWS Lambda" workflow from the Actions tab in GitHub.

## Automatic Updates

The service automatically checks for updates daily at midnight UTC. When new data is available:

1. Downloads the latest data from the source repository
2. Updates version and term information
3. Creates a pull request with the changes
4. Automatically deploys to AWS Lambda after the PR is merged

## Environment Setup

### Required Secrets

Add the following secret to your GitHub repository:

- `AWS_ROLE_ARN`: The ARN of the IAM role for GitHub Actions

### AWS Configuration

1. Create an AWS Lambda function named `suchedule-service`
2. Create a production alias
3. Configure the IAM role with necessary permissions:
   - `lambda:UpdateFunctionCode`
   - `lambda:ListVersionsByFunction`
   - `lambda:UpdateAlias`
   - `lambda:InvokeFunction`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Data source: [SUchedule](https://github.com/aburakayaz/suchedule) by @aburakayaz
