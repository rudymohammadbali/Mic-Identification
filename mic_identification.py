import soundcard


class MicIdentification:
    """Class for identifying connected microphones."""

    def __init__(self):
        self.microphones = self.get_connected_microphones()

    def get_connected_microphones(self):
        """Retrieve the list of connected microphones.

        Returns:
            list: List of tuples representing connected microphones,
            where each tuple contains the microphone name and index.
        """
        input_devices = soundcard.all_microphones()
        connected_microphones = [
            (device.name, i) for i, device in enumerate(input_devices)
        ]
        return connected_microphones

    def search_microphone(self, by_name=None, by_index=None):
        """Search for a microphone based on name or index.

        Args:
            by_name (str, optional): Name or partial name of the microphone to search for.
            by_index (int, optional): Index of the microphone to search for.

        Raises:
            ValueError: If both by_name and by_index arguments are None.

        Returns:
            None
        """
        if by_name is None and by_index is None:
            raise ValueError(
                "At least one of by_name and by_index arguments must be provided."
            )

        if by_index is not None:
            if not isinstance(by_index, int):
                raise TypeError("Invalid by_index argument. Integer value expected.")

            found_mic = self.find_microphone_by_index(by_index)
            if found_mic is not None:
                self.print_microphone(found_mic)
            else:
                print(f"No microphone found with index {by_index}.")
            return

        if by_name is not None:
            if not isinstance(by_name, str):
                raise TypeError("Invalid by_name argument. String value expected.")

            matches = self.find_microphones_by_name(by_name)
            if matches:
                self.print_microphones(matches)
            else:
                print(f"No microphones found with name containing '{by_name}'.")

    def find_microphone_by_index(self, index):
        """Find a microphone by its index.

        Args:
            index (int): Index of the microphone to find.

        Returns:
            tuple: A tuple representing the microphone (name, index) if found, else None.
        """
        for mic in self.microphones:
            if index == mic[1]:
                return mic
        return None

    def find_microphones_by_name(self, name):
        """Find microphones by name or partial name.

        Args:
            name (str): Name or partial name of the microphones to find.

        Returns:
            list: List of tuples representing the matching microphones (name, index).
        """
        matches = []
        for mic in self.microphones:
            if name.lower() in mic[0].lower():
                matches.append(mic)
        return matches

    def print_microphone(self, mic):
        """Print the details of a single microphone.

        Args:
            mic (tuple): A tuple representing the microphone (name, index).

        Returns:
            None
        """
        print(f"Microphone found - Name: {mic[0]}, Index: {mic[1]}")

    def print_microphones(self, microphones):
        """Print the details of multiple microphones.

        Args:
            microphones (list): List of tuples representing the microphones (name, index).

        Returns:
            None
        """
        print("Microphones found:")
        for mic in microphones:
            print(f"Name: {mic[0]}, Index: {mic[1]}")


# Usage
# mic_identification = MicIdentification()
# print(mic_identification.get_connected_microphones()) # Example usage: get list of all connected microphones
# mic_identification.search_microphone(by_index=0)  # Example usage: searching by index
# mic_identification.search_microphone(by_name="Microphone")  # Example usage: searching by name
