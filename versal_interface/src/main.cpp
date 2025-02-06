#include <iostream>
#include <chrono>
#include <functional>
#include <memory>
#include <thread>
#include <fstream>

#include <cstdio>
#include <string.h>
#include <stdlib.h>
// Linux headers
#include <fcntl.h> // Contains file controls like O_RDWR
#include <errno.h> // Error integer and strerror() function
#include <termios.h> // Contains POSIX terminal control definitions
#include <unistd.h> // write(), read(), close()

int configure_serial(int *serial_port, struct termios *tty) {
   // Read in existing settings, and handle any error
      if(tcgetattr(*serial_port, tty) != 0) {
          printf("Error %i from tcgetattr: %s\n", errno, strerror(errno));
          return 1;
      }

      tty->c_cflag &= ~PARENB; // Clear parity bit, disabling parity (most common)
      tty->c_cflag &= ~CSTOPB; // Clear stop field, only one stop bit used in communication (most common)
      tty->c_cflag &= ~CSIZE; // Clear all bits that set the data size
      tty->c_cflag |= CS8; // 8 bits per byte (most common)
      tty->c_cflag &= ~CRTSCTS; // Disable RTS/CTS hardware flow control (most common)
      tty->c_cflag |= CREAD | CLOCAL; // Turn on READ & ignore ctrl lines (CLOCAL = 1)

      tty->c_lflag &= ~ICANON;
      tty->c_lflag &= ~ECHO; // Disable echo
      tty->c_lflag &= ~ECHOE; // Disable erasure
      tty->c_lflag &= ~ECHONL; // Disable new-line echo
      tty->c_lflag &= ~ISIG; // Disable interpretation of INTR, QUIT and SUSP
      tty->c_iflag &= ~(IXON | IXOFF | IXANY); // Turn off s/w flow ctrl
      tty->c_iflag &= ~(IGNBRK|BRKINT|PARMRK|ISTRIP|INLCR|IGNCR|ICRNL); // Disable any special handling of received bytes

      tty->c_oflag &= ~OPOST; // Prevent special interpretation of output bytes (e.g. newline chars)
      tty->c_oflag &= ~ONLCR; // Prevent conversion of newline to carriage return/line feed
      // tty.c_oflag &= ~OXTABS; // Prevent conversion of tabs to spaces (NOT PRESENT ON LINUX)
      // tty.c_oflag &= ~ONOEOT; // Prevent removal of C-d chars (0x004) in output (NOT PRESENT ON LINUX)

      tty->c_cc[VTIME] = 10;    // Wait for up to 1s (10 deciseconds), returning as soon as any data is received.
      tty->c_cc[VMIN] = 0;

      // Set in/out baud rate to be 115200
      cfsetispeed(tty, B115200);
      cfsetospeed(tty, B115200);

      // Save tty settings, also checking for error
      if (tcsetattr(*serial_port, TCSANOW, tty) != 0) {
          printf("Error %i from tcsetattr: %s\n", errno, strerror(errno));
          return 1;
      }
      return 0;
}

#define SERIAL_PORT "/dev/pts/13"
int main() {
	std::cout << "Hello There \n";

    std::cout << "Open serial Port \n";
    std::ofstream serialOut(SERIAL_PORT);

    if (!serialOut.is_open()) {
        std::cerr << "Error: Cannot open serial port " << SERIAL_PORT << std::endl;
        return 1;
    }
    int count = 0;
    while (true) {
        serialOut << count++ << std::endl;
        serialOut.flush();  // Ensure data is sent
        std::cout << "Sent: Message #" << count << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    /*
    int serial_port = open("/dev/pts/13", O_RDWR); 

	struct termios tty;
    std::cout << "Done \n";

	int status;

    std::cout << "Config Serial \n";
	status = configure_serial(&serial_port,&tty);

    std::cout << "Done with status:"<< status <<"\n";
	char message_buf[20], *ptr;

    char msg = '1';
    int counter = 0;
    while(1) {
	    memset(&message_buf, '\0', sizeof(message_buf));
        ptr = message_buf;
        write(serial_port, &msg, sizeof(msg));
        //msg = counter;
        if(counter == 100)
            counter = 0;
        counter++;
        std::cout<< msg <<"\n";    
        /*
        int bytes_left = sizeof(message_buf);
        while(bytes_left != 0) {
            int num_bytes = read(serial_port, ptr, bytes_left);
            bytes_left -= num_bytes;
            ptr += num_bytes;
        }
        std::cout << message_buf;
        *
       std::this_thread::sleep_for(std::chrono::seconds(1));
    }
	*/
	return 0;
}
