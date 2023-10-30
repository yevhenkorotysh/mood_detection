# Mood Detection Service from Audio Files

This application aims to build a Mood Detection Service from audio files, providing two main services:

1. **Service to Store an Audio File:**
Users can upload an audio file, which is then securely stored in a cloud storage system, such as AWS S3.

2. **Service to Retrieve Mood:**
The second service analyzes the uploaded audio file to determine the mood and returns
one of three different moods: Happy, Sad, or Calm. In this project, a random mood generator is used as a placeholder.

## Architecture

### Language Choice

The service code is implemented in Python/Django due to its extensive libraries and ease of use for audio processing.

### Components

The project architecture comprises several key components:

1. **Audio File Storage:** Cloud storage, specifically AWS S3, is used to store uploaded audio files.
Uploaded files must be in WAV or MP3 format and limited to a maximum duration of 30 seconds.

2. **Audio Processing:**
For mood analysis, the uploaded audio file is processed. In this example, a random mood is generated.
In a real implementation, audio analysis would involve libraries like Librosa for feature extraction and
potentially AI model training.

3. **Developer Console Testing:**
Both services can be tested using the following links:

   **Basic User Interface (Browser):**
   - [Upload Page](http://moody-env.eba-3u6gpwmy.us-west-2.elasticbeanstalk.com/upload/)
   - [Audio List](http://moody-env.eba-3u6gpwmy.us-west-2.elasticbeanstalk.com/api/audio_list/)

   **API (Requires Postman):**
   - [Audio List](http://moody-env.eba-3u6gpwmy.us-west-2.elasticbeanstalk.com/api/audio_list/)
   - [Audio Add](http://moody-env.eba-3u6gpwmy.us-west-2.elasticbeanstalk.com/api/audio_add/)
   - [Audio Details](http://moody-env.eba-3u6gpwmy.us-west-2.elasticbeanstalk.com/api/audio_details/{id}/)

### Cloud Services

- **AWS S3:** AWS S3 file storage is used to securely and efficiently store audio files. It can be seamlessly scaled, performs quickly, and is cost-efficient.

- **AWS RDS:** The database is hosted on a cloud service, Amazon RDS (Relational Database Service).

### Project Deployment

This project is deployed on AWS EC2.
You can test it by following this link: [Mood Detection Service](http://moody-env.eba-3u6gpwmy.us-west-2.elasticbeanstalk.com).

### Project Structure

The application's design and code structure can be found in the [Application Design Document]
(https://docs.google.com/drawings/d/1lz_G_nxaQ3Wu5mwoQipgYEkwpSbnIDoKOrsfcFwUtu4/edit?usp=sharing).
This document provides an in-depth understanding of the architecture, data flow, and application components.

### Testing

Unit tests and integration tests for the service code should be provided in the project's `tests` directory.
These tests are essential to ensure the reliability and correctness of the code.

### Improvements

For potential improvements, consider the following:

- Collaborating closely with Company Data Engineers and Data Scientists to implement best practices of data collection, ensuring that the app collects and stores data in proper formats.

- Implementing a real mood analysis algorithm for more accurate mood detection.

- Collaborating with front-end engineers to enhance the user interface for a better user experience.

- Adding support for more audio formats to increase compatibility.

- Implementing user authentication and authorization for secure file uploads.

- Unit tests

For any clarification, sample data, or further questions, please feel free to reach out.
