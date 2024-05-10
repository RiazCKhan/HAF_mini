import SupportAgentIcon from "@mui/icons-material/SupportAgent";
import Diversity3Icon from "@mui/icons-material/Diversity3";
import HealthAndSafetyIcon from "@mui/icons-material/HealthAndSafety";
import LocalShippingIcon from "@mui/icons-material/LocalShipping";

export const LeftBarStatic = [
  {
    id: "agent",
    title: "Agent",
    icon: <SupportAgentIcon />,
    link: "/agents"
  },
  {
    id: "client",
    title: "Client",
    icon: < Diversity3Icon />,
    link: "/clients"
  },
  {
    id: "referral",
    title: "Referral",
    icon: <HealthAndSafetyIcon />,
    link: "/referrals"
  },
  {
    id: "delivery",
    title: "Delivery",
    icon: <LocalShippingIcon />,
    link: "/deliveries"
  }
]
