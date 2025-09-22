## Mini Project - Hostel Visit Recording System with Check-in/Check-out

from datetime import datetime

class Visitor:
    """Class to represent a visitor with name and ID"""
    def __init__(self, name, visitor_id):
        self.name = name
        self.visitor_id = visitor_id
    
    def __str__(self):
        return f"Visitor: {self.name} (ID: {self.visitor_id})"

class Resident:
    """Class to represent a resident with name and room"""
    def __init__(self, name, room):
        self.name = name
        self.room = room
    
    def __str__(self):
        return f"Resident: {self.name} (Room: {self.room})"

class Hostel:
    """Class to represent a hostel that records visits with check-in/check-out system"""
    def __init__(self, name):
        self.name = name
        self.completed_visits = []  # List to store completed visits with duration
        self.active_visits = {}     # Dict to track currently active visits
    
    def check_in(self, visitor, resident):
        """Check in a visitor to visit a resident"""
        visit_key = f"{visitor.visitor_id}_{resident.room}"
        
        # Check if visitor is already checked in somewhere
        for key in self.active_visits:
            if key.startswith(visitor.visitor_id):
                print(f"Error: {visitor.name} is already checked in! Please check out first.")
                return False
        
        # Record check-in
        check_in_time = datetime.now()
        self.active_visits[visit_key] = {
            'visitor': visitor,
            'resident': resident,
            'check_in_time': check_in_time
        }
        
        print(f"CHECK-IN: {visitor.name} checked in to visit {resident.name} in room {resident.room}")
        print(f"   Time: {check_in_time.strftime('%Y-%m-%d %H:%M:%S')}")
        return True
    
    def check_out(self, visitor, resident):
        """Check out a visitor and calculate visit duration"""
        visit_key = f"{visitor.visitor_id}_{resident.room}"
        
        if visit_key not in self.active_visits:
            print(f"Error: No active visit found for {visitor.name} in room {resident.room}")
            return False
        
        # Get visit details and calculate duration
        visit_info = self.active_visits[visit_key]
        check_out_time = datetime.now()
        duration = check_out_time - visit_info['check_in_time']
        
        # Create completed visit record
        completed_visit = {
            'visitor': visitor,
            'resident': resident,
            'check_in_time': visit_info['check_in_time'],
            'check_out_time': check_out_time,
            'duration': duration
        }
        
        # Move from active to completed visits
        self.completed_visits.append(completed_visit)
        del self.active_visits[visit_key]
        
        print(f"CHECK-OUT: {visitor.name} checked out from {resident.name}'s room")
        print(f"   Duration: {self._format_duration(duration)}")
        return True
    
    def record_visit(self, visitor, resident):
        """Legacy method - now uses check-in system"""
        print("Note: Using new check-in system...")
        return self.check_in(visitor, resident)
    
    def show_active_visits(self):
        """Display all currently active visits"""
        if not self.active_visits:
            print(f"\nNo active visits at {self.name}")
            return
        
        print(f"\n === Active Visits at {self.name} ===")
        for i, (key, visit) in enumerate(self.active_visits.items(), 1):
            visitor = visit['visitor']
            resident = visit['resident']
            check_in_time = visit['check_in_time']
            current_duration = datetime.now() - check_in_time
            
            print(f"{i}. {visitor.name} (ID: {visitor.visitor_id}) visiting {resident.name} in room {resident.room}")
            print(f"   Checked in: {check_in_time.strftime('%H:%M:%S')} | Current duration: {self._format_duration(current_duration)}")
    
    def show_visits(self):
        """Display all completed visits with durations"""
        if not self.completed_visits:
            print(f"\n No completed visits recorded for {self.name}")
            return
        
        print(f"\n === Completed Visit Records for {self.name} ===")
        total_duration = 0
        
        for i, visit in enumerate(self.completed_visits, 1):
            visitor = visit['visitor']
            resident = visit['resident']
            check_in = visit['check_in_time'].strftime('%Y-%m-%d %H:%M:%S')
            check_out = visit['check_out_time'].strftime('%Y-%m-%d %H:%M:%S')
            duration = visit['duration']
            total_duration += duration.total_seconds()
            
            print(f"{i}. {visitor.name} (ID: {visitor.visitor_id}) visited {resident.name} in room {resident.room}")
            print(f"   Check-in: {check_in}")
            print(f"   Check-out: {check_out}")
            print(f"   Duration: {self._format_duration(duration)}")
            print()
        
        print(f" Total visit time: {self._format_duration_seconds(total_duration)}")
    
    def get_visitor_status(self, visitor):
        """Check if a visitor is currently checked in"""
        for key, visit in self.active_visits.items():
            if visit['visitor'].visitor_id == visitor.visitor_id:
                resident = visit['resident']
                duration = datetime.now() - visit['check_in_time']
                print(f" {visitor.name} is currently visiting {resident.name} in room {resident.room}")
                print(f"   Duration so far: {self._format_duration(duration)}")
                return True
        
        print(f" {visitor.name} is not currently checked in")
        return False
    
    def _format_duration(self, duration):
        """Format duration in a readable way"""
        total_seconds = int(duration.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        if hours > 0:
            return f"{hours}h {minutes}m {seconds}s"
        elif minutes > 0:
            return f"{minutes}m {seconds}s"
        else:
            return f"{seconds}s"
    
    def _format_duration_seconds(self, total_seconds):
        """Format total seconds into readable duration"""
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        
        if hours > 0:
            return f"{hours}h {minutes}m {seconds}s"
        elif minutes > 0:
            return f"{minutes}m {seconds}s"
        else:
            return f"{seconds}s"

# Demo - Enhanced system with check-in/check-out
if __name__ == "__main__":
    # Create instances
    visitor1 = Visitor('Alice', 'V123')
    visitor2 = Visitor('John', 'V456')
    visitor3 = Visitor('Mary', 'V789')
    
    resident1 = Resident('Bob', '12B')
    resident2 = Resident('Sarah', '15A')
    resident3 = Resident('Mike', '10C')
    
    hostel = Hostel('UCU Hostel')
    
    print(" === UCU Hostel Visit Management System ===\n")
    
    # Demo 1: Basic check-in/check-out
    print(" Demo 1: Basic Check-in/Check-out")
    hostel.check_in(visitor1, resident1)
    
    # Show active visits
    hostel.show_active_visits()
    
    # Simulate some time passing (in real scenario, there would be actual time gap)
    import time
    time.sleep(2)  # Wait 2 seconds to show duration
    
    # Check out
    hostel.check_out(visitor1, resident1)
    
    print("\n" + "="*60)
    
    # Demo 2: Multiple visitors
    print(" Demo 2: Multiple Visitors")
    hostel.check_in(visitor2, resident2)
    hostel.check_in(visitor3, resident3)
    
    # Try to check in same visitor again (should fail)
    hostel.check_in(visitor2, resident1)
    
    # Show current active visits
    hostel.show_active_visits()
    
    # Check visitor status
    hostel.get_visitor_status(visitor2)
    hostel.get_visitor_status(visitor1)  # Should show not checked in
    
    print("\n" + "="*60)
    
    # Demo 3: Complete some visits
    print(" Demo 3: Completing Visits")
    time.sleep(1)
    hostel.check_out(visitor2, resident2)
    
    time.sleep(1)
    hostel.check_out(visitor3, resident3)
    
    # Show all completed visits with durations
    hostel.show_visits()
    
    print("\n" + "="*60)
    
    # Demo 4: More complex scenario
    print(" Demo 4: Extended Visit Tracking")
    
    # Alice visits Bob again
    hostel.check_in(visitor1, resident1)
    time.sleep(2)
    
    # John visits Mike
    hostel.check_in(visitor2, resident3)
    time.sleep(1)
    
    # Show active visits
    hostel.show_active_visits()
    
    # Check out both
    hostel.check_out(visitor1, resident1)
    hostel.check_out(visitor2, resident3)
    
    # Final summary
    print("\n" + "="*60)
    print(" Final Visit Summary:")
    hostel.show_visits()
    
    print(f"\nTotal visitors served: {len(set([v['visitor'].name for v in hostel.completed_visits]))}")
    print(f"Total completed visits: {len(hostel.completed_visits)}")
    print(f"Currently active visits: {len(hostel.active_visits)}")